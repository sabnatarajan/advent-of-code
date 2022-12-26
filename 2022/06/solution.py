from pathlib import Path

def start_packet(msg: str, length=4): 
  j = length
  while j < len(msg):
    sub_msg = set(msg[j-length:j])
    if len(sub_msg) == length:
      return j
    j += 1
  
if __name__ == "__main__":
  assert start_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
  assert start_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
  assert start_packet("nppdvjthqldpwncqszvftbrmjlhg") == 6
  assert start_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
  assert start_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

  assert start_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
  assert start_packet("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
  assert start_packet("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
  assert start_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
  assert start_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

  with open(Path(__file__).parent / Path("input.txt")) as f:
    msg = f.read()
    start = start_packet(msg)
    print(f"Part 1: {start}")
    print(f"Part 2: {start_packet(msg, 14)}")