#include <iostream>
#include "primes.hpp"

namespace {

    // registers a-h
    int b = 81,
        c = 81,
        e = 0,
        counter = 0; // h is only used for counting so renaming for clarity

    bool debug_mode = false;

    int mul = 0;
}

void print_registers() {
    std::cout
        << "[\n"
        << "  a: " << debug_mode << '\n'
        << "  b: " << b << '\n'
        << "  c: " << c << '\n'
        << "  e: " << e << '\n'
        << "  h: " << counter << '\n'
        << "]\n";
}

void func1() {
    while (true) {
        //bool should_inc_counter = false; // f is only used as a flag and can be made local

        // d and e can be locals
        // they are only used for looping
        /*
        for (int d = 2; d != b; d += 1) {
            for (int e = 2; e != b; e += 1) {

                mul += 1;

                if (d * e == b) { // checks if d or e is  factor of b
                    should_inc_counter = true;
                    break; // Can break early
                }
            }
        }
        */

        // replace nested loops above with prime check
        bool is_prime = primes_set.find(b) != primes_set.end();

        if (!is_prime) {
            // this counter is only incremented based on the loop above
            // in effect the check above is incrementing the counter if
            // the register b has a factor between 2 and b, in other words
            // if b is not a prime we can increment this counter
            counter += 1;
        }

        if (c == b) {
            break;
        }

        b += 17;
    }
}

void func2() {
    b = 108100;
    c = 125100;

    mul += 1;
}

int main(int argc, char *argv[]) {

    if (argc > 1) {
        std::string str(argv[1]);
        if (str == "debug") {
            debug_mode = true; //a = 1;
        }
    }

    if (debug_mode) {
        func2();
    }

    func1();

    std::cout << "MUL: " << mul << '\n';
    std::cout << "H: " << counter << '\n';

    return 0;
}
