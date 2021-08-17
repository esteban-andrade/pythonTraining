
void solution(int N, int R[], int C[], int M)
{
    // write your code in C99 (gcc 6.2.0)
    int row, col;
    int count = 0;

    int x = N;
    int y = N;
    int **field = malloc(x * sizeof(int *));
    for (int i = 0; i < y; i++)
    {
        field[i] = malloc(sizeof(int *) * y);
    }

    int **counter = malloc(x * sizeof(int *));
    for (int i = 0; i < y; i++)
    {
        counter[i] = malloc(sizeof(int *) * y);
    }

    int num = sizeof R / sizeof *R;

    for (int i = 0; i < N; i++)
    {

        for (int j = 0; j < N; j++)
        {
            for (int z = 0; z < num; z++)
                field[R[num]][C[num]] = 'B';
        }
    }

    for (int x = 0; x < N; x++) {
			for (int y = 0; y < N; y++) 
				counter[x][y] = 0;
		}




        //CASES
		for (int row = 0; row < N; row++) {
			for (int col = 0; col < N; col++) {
				if (field[row][col] == 'B') {

					counter[row - 1][col - 1]++;
					counter[row - 1][col]++;
					counter[row - 1][col + 1]++;
					counter[row][col - 1]++;
					counter[row][col + 1]++;
					counter[row + 1][col - 1]++;
					counter[row + 1][col]++;
					counter[row + 1][col + 1]++;
					
				}
			}
		}

        for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (field[r][c] == 'B')
					printf('B');
				else
					printf("%d" ,counter[r][c]);
			}
			
		}
		
	
	return 0;
}
