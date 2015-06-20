#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LENGTH 100
#define BOARD_DIMENSION_SIZE 256
#define COMMAND_COUNT 3
#define COMMAND_MAX_LENGTH 20

int main(int agrc, char * argv[])
{
    char line[LINE_LENGTH];
    char commands[COMMAND_COUNT][COMMAND_MAX_LENGTH];
    unsigned char rowIndex = 0;
    unsigned char colIndex = 0;

    unsigned short index = 0;
    unsigned short board[BOARD_DIMENSION_SIZE][BOARD_DIMENSION_SIZE];
    unsigned short colSum = 0;
    unsigned short rowSum = 0;

    char * token = NULL;
    FILE * file = NULL;

    memset(board, 0, (BOARD_DIMENSION_SIZE * BOARD_DIMENSION_SIZE) * sizeof(unsigned short));
    memset(commands, '0', COMMAND_COUNT * COMMAND_MAX_LENGTH);
    memset(line, '0', LINE_LENGTH);

    file = fopen(argv[1], "r");

    while(fgets(line, LINE_LENGTH, file))
    {
        token = strtok(line, " ");
        index = 0;

        while(token)
        {
            strcpy(commands[index], token);
            index++;
            token = strtok(NULL, " ");
        }

        if(strcmp(commands[0], "SetCol") == 0)
        {
            colIndex = atoi(commands[1]);
            for(index = 0; index < BOARD_DIMENSION_SIZE; ++index)
            {
                board[index][colIndex] = atoi(commands[2]);
            }

        }else if(strcmp(commands[0], "SetRow") == 0)
        {
            rowIndex = atoi(commands[1]);
            for(index = 0; index < BOARD_DIMENSION_SIZE; ++index)
            {
                board[rowIndex][index] = atoi(commands[2]);
            }
        }else if(strcmp(commands[0], "QueryCol") == 0)
        {
            colIndex = atoi(commands[1]);
            colSum = 0;
            for(index = 0; index < BOARD_DIMENSION_SIZE; ++index)
            {
                colSum += board[index][colIndex];
            }
            printf("%d\n", colSum);
        }else if(strcmp(commands[0], "QueryRow") == 0)
        {
            rowIndex = atoi(commands[1]);
            rowSum = 0;
            for(index = 0; index < BOARD_DIMENSION_SIZE; ++index)
            {
                rowSum += board[rowIndex][index];
            }
            printf("%d\n", rowSum);
        }
    }
    fclose(file);
    return 0;
}