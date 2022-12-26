from typing import Tuple, List
from pathlib import Path
from enum import Enum

class CmdType(Enum):
  none = "none"
  cd = "cd"
  ls = "ls"

  @staticmethod
  def parse(line: str) -> Tuple["CmdType", str]:
    if not line.startswith("$"): return None, line
    cmd = line.replace("$", "").strip()
    splits = cmd.split()
    try:
      cmdtype = CmdType[splits[0]]
    except Exception:
      cmdtype = CmdType.none

    cmd = None
    if cmdtype == CmdType.cd:
      cmd = splits[1]

    return cmdtype, cmd

class FileType(Enum):
  FILE = 1
  DIR = 2
  
class Node:
  def __init__(self, name, ftype: FileType=FileType.DIR, size=0, parent: "Node"=None):
    self.name = name
    self.parent = parent
    self.ftype = ftype
    
    self.size = size
    self.children: List[Node] = []

  def add(self, node: "Node"):
    node.parent = self
    children_names = [_.name for _ in self.children]
    if node.name not in children_names:
      self.children.append(node)
    
  def __repr__(self) -> str:
    if not self.parent:
      parent_name = "None"
    else:
      parent_name = self.parent.name
    return f"Node(name={self.name}, ftype={self.ftype.name}, size={self.size}, parent={parent_name}, children={len(self.children)})"

  def get_size(self, size=0):
    if not self.children:
      return self.size

    for c in self.children:
      size += c.get_size()

    return self.size + size

def dfs(node: Node, nodes=set()):
  if not node.children:
    return

  for child in node.children:
    if child.ftype == FileType.DIR:
      nodes.add(child)
      dfs(child, nodes)
  
  return nodes

if __name__ == "__main__":
  with open(Path(__file__).parent / Path("input.txt")) as f:
    lines = f.readlines()

  root = Node('/')
  curdir = root

  for line in lines:
    line = line.strip()
    cmdtype, cmd = CmdType.parse(line)
    
    if cmdtype == CmdType.cd:
      dirname = cmd
      if dirname == "/": # go to root
        curdir = root
      elif dirname == "..": # go up 1 level
        curdir = curdir.parent
      else: # goto to specified dir
        # search for this dir among the neighbors or add a new one
        for c in curdir.children:
          if c.name == dirname:
            curdir = c
            break
        else: # for's else
          newdir = Node(dirname, parent=curdir)
          curdir.add(newdir)
        
    elif cmdtype == CmdType.ls:
      # mark that ls output needs to be parsed
      # curdir.add(Node())
      pass
    else:
      # parse the ls output
      splits = cmd.split()
      if splits[0] == "dir":
        n = Node(name=splits[1], ftype=FileType.DIR, size=0, parent=curdir.parent)
        curdir.add(n)
      else:
        n = Node(name = splits[1], ftype=FileType.FILE, size=int(splits[0]), parent=curdir.parent)
        curdir.add(n)

  dirs_under100k_size = 0
  dir_sizes = set()
  for dir in dfs(root):
    s = dir.get_size()
    dir_sizes.add(s)
    if s <= 100_000:
      dirs_under100k_size += s

  print(f"Part 1: {dirs_under100k_size}")
  
  # Part 2
  total_space = 70_000_000
  needed_space = 30_000_000
  used_space = root.get_size()
  unused_space = total_space - used_space
  dir_sizes = sorted(dir_sizes)

  smallest = 2**31-1
  for i, size in enumerate(dir_sizes):
    new_unused = unused_space + size
    if new_unused > needed_space and size < smallest:
      smallest = size
  
  print(f"Part 2: {smallest}")
