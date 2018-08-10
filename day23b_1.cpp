#include <iostream>

namespace {
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    int e = 0;
    int f = 0;
    int g = 0;
    int h = 0;
    int mul = 0;
}

int main() {

    b = 81;                 // set b 81
    c = b;                  // set c b
    if (a) {                // jnz a 2
        goto jump_1;
    }
    if (1) {
        goto jump_2;        // jnz 1 5
    }
jump_1:
    b = b * 100;            // mul b 100
        mul += 1;
    b = b - -100000;        // sub b -100000
    c = b;                  // set c b
    c = c - -17000;         // sub c -17000
jump_2:
    f = 1;                  // set f 1
    d = 2;                  // set d 2
jump_5:
    e = 2;                  // set e 2
jump_4:
    g = d;                  // set g d
    g = g * e;              // mul g e
        mul += 1;
    g = g - b;              // sub g b
    if (g) {                // jnz g 2
        goto jump_3;
    }
    f = 0;                  // set f 0
jump_3:
    e = e - -1;             // sub e -1
    g = e;                  // set g e
    g = g - b;              // sub g b
    if (g) {                // jnz g -8
        goto jump_4;
    }
    d = d - -1;             // sub d -1
    g = d;                  // set g d
    g = g - b;              // sub g b
    if (g) {                // jnz g -13
        goto jump_5;
    }
    if (f) {                // jnz f 2
        goto jump_6;
    }
    h = h - -1;             // sub h -1
jump_6:
    g = b;                  // set g b
    g = g - c;              // sub g c
    if (g) {                // jnz g 2
        goto jump_7;
    }
    if (1) {                // jnz 1 3
        goto end;
    }
jump_7:
    b = b - -17;            // sub b -17
    if (1) {                // jnz 1 -23
        goto jump_2;
    }
end:

    std::cout << "mul: " << mul << '\n';
    return 0;
}
