#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_TRIALS 1000000

// Function to simulate rolling two dice and computing probabilities
void calculate_probabilities(double *P_AB, double *P_BC, double *P_CA) {
    int count_AB = 0, count_BC = 0, count_CA = 0;
    
    for (int i = 0; i < NUM_TRIALS; i++) {
        int x = (rand() % 6) + 1;
        int y = (rand() % 6) + 1;
        
        int sum = x + y;
        int event_A = (sum > 8);
        int event_B = (x == 2 || y == 2);
        int event_C = (sum >= 7 && sum % 3 == 0);
        
        if (event_A && event_B) count_AB++;
        if (event_B && event_C) count_BC++;
        if (event_C && event_A) count_CA++;
    }
    
    *P_AB = (double)count_AB / NUM_TRIALS;
    *P_BC = (double)count_BC / NUM_TRIALS;
    *P_CA = (double)count_CA / NUM_TRIALS;
}

int main() {
    srand(time(NULL));
    double P_AB, P_BC, P_CA;
    
    calculate_probabilities(&P_AB, &P_BC, &P_CA);
    
    printf("%lf %lf %lf\n", P_AB, P_BC, P_CA);
    
    return 0;
}
