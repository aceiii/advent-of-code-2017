#include <iostream>

namespace {

    // registers a-h
    int //a = 0,
        b = 81,
        c = 81,
        //d = 0,
        e = 0,
        //f = 0,
        //g = 0,
        counter = 0; //h = 0;

    bool debug_mode = false;
         //should_inc_counter = false;

    int mul = 0;
}

void print_registers() {
    std::cout
        << "[\n"
        << "  a: " << debug_mode << '\n'
        << "  b: " << b << '\n'
        << "  c: " << c << '\n'
        //<< "  d: " << d << '\n'
        << "  e: " << e << '\n'
        //<< "  f: " << should_inc_counter << '\n'
        //<< "  g: " << g << '\n'
        << "  h: " << counter << '\n'
        << "]\n";
}

void func1() {
    while (true) {
        bool should_inc_counter = false;

        //d = 2;

        //bool reset = true;

        for (int d = 2; d != b; d += 1) {
        //do {
            //print_registers();

            for (int e = 2; e != b; e += 1) {
                /*
            if (reset) {
                reset = false;
                e = 2;
            }
            */

            //g = (d * e) - b;
            mul += 1;

            //if ((d * e) - b == 0) {
            if (d * e == b) {
                //std::cout << "should_inc_counter\n";
                std::cout << "break (d: " << d << ", e: " << e << ", b: " << b << ")\n";
                should_inc_counter = true;
                //break;
            }

            //e += 1;
            //g = e - b;

            //std::cout << "g1: " << g << '\n';
            //if (g) {
            //std::cout << "e: " << e << ", b: " << b << '\n';
            /*
            if (e - b) {
                d -= 1;
                continue;
            }
            */
            }

            //d += 1;
            //g = d - b;

            //reset = true;

            //std::cout << "g2: " << g << '\n';
            //std::cout << "(d: " << d << ", b: " << b << ")\n";
        //} while (g);
        //} while (d - b);

        }

        std::cout << "(b: " << b << ")\n";
        if (should_inc_counter) {    // if (f == 0) // reversed value when setting
            counter += 1;
        }

        //g = b - c;


        //std::cout << "h: " << counter << '\n';
        //std::cout << "b: " << b << ", c: " << c << ", h: " << counter << '\n';
        //if (g) {
        /*
        if (b - c) {
            b += 17;
        } else {
            break;
        }
        */

        if (c == b) {
            break;
        }

        b += 17;
    }
}

void func2() {
    //b = 108100;
    //c = 125100;
    b = 81;
    c = 81 + (17 * 10);

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
