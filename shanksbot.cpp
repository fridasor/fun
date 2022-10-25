#include <iostream>
#include <vector>

/**
 * Calculate the how many digits there are in
 * the reciprocal of a given prime number.
 *
 * @param num A prime number.
 * @return Number of digits in the period of the reciprocal of the prime.
 */
int reciprocals(int num) {
  std::vector<int> rests;
  int rest;
  bool dividing = true;

  int top = 1;

  while (dividing) {
    if (num > top) {
      top *= 10;
    }
    if (top / num >= 0) {
      rest = top % num;

      if (std::find(rests.begin(), rests.end(), rest) != rests.end()) {
        dividing = false;
        break;
      }
      rests.push_back(rest);
      top = rest;
    }
  }

  return rests.size();
}

int main(int argc, char* argv[]) {
  int num = atoi(argv[1]);
  std::cout << reciprocals(num) << std::endl;

  return 0;
}
