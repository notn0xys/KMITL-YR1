#include <iostream>
#include <vector>
#include <ctime>
#include <stack>

#define SIZE 15

using namespace std;

struct Point {
    int x, y;
};

vector<vector<char>> maze(SIZE, vector<char>(SIZE, '#'));
Point entry, exitPoint;
vector<vector<bool>> visited(SIZE, vector<bool>(SIZE, false));

void generateMaze() {
    srand(time(0));
    for (int i = 1; i < SIZE - 1; i += 2) {
        for (int j = 1; j < SIZE - 1; j += 2) {
            maze[i][j] = '.';
            if (rand() % 2) {
                if (i + 1 < SIZE - 1) maze[i + 1][j] = '.';
            } else {
                if (j + 1 < SIZE - 1) maze[i][j + 1] = '.';
            }
        }
    }
    entry = {0, 1};
    exitPoint = {SIZE - 1, SIZE - 2};
    maze[entry.x][entry.y] = '.';
    maze[exitPoint.x][exitPoint.y] = '.';
}

bool solveMaze(Point start) {
    stack<Point> s;
    s.push(start);
    visited[start.x][start.y] = true;
    while (!s.empty()) {
        Point p = s.top();
        if (p.x == exitPoint.x && p.y == exitPoint.y) return true;
        s.pop();
        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};
        for (int i = 0; i < 4; i++) {
            int nx = p.x + dx[i], ny = p.y + dy[i];
            if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE && !visited[nx][ny] && maze[nx][ny] == '.') {
                visited[nx][ny] = true;
                maze[nx][ny] = '*'; // Mark path
                s.push({nx, ny});
            }
        }
    }
    return false;
}

void printMaze() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            cout << maze[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    generateMaze();
    solveMaze(entry);
    printMaze();
    return 0;
}
