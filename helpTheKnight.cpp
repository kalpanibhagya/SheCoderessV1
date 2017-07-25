#include <bits/stdc++.h>
using namespace std;
#define N 8
 
int row[] = { 2, 2, -2, -2, 1, 1, -1, -1 };
int col[] = { -1, 1, 1, -1, 2, -2, 2, -2 };
 
bool validation(int x, int y)
{
	if (x < 0 || y < 0 || x >= N || y >= N)
		return false;
 
	return true;
}
 
struct Node
{
	int x, y, dist;
	
	bool const operator==(const Node& o) const
	{
		return x == o.x && y == o.y;
	}
 
	bool operator<(const Node& o) const
	{
		return x < o.x || (x == o.x && y < o.y);
	}
};
 
int BFS(Node src, Node dest)
{
	map<Node, bool> visited;
	
	queue<Node> q;
	q.push(src);
 
	while (!q.empty())
	{
		Node node = q.front();
		q.pop();
 
		int x = node.x;
		int y = node.y;
		int dist = node.dist;
		
		if (x == dest.x && y == dest.y)
			return dist;
 
		if (!visited.count(node))
		{
			visited[node] = true;
 
			for (int i = 0; i < 8; ++i) 
			{
				int x1 = x + row[i];
				int y1 = y + col[i];
 
				if (validation(x1, y1))
					q.push({x1, y1, dist + 1});
			}
		}
	}
 
	return INT_MAX;
}
 
int main()
{
	string s;
	cin >> s;
	string d;
	cin >> d;
 
	char s1 = s[1];
	char s2 = s[3];
	char d1 = d[1];
	char d2 = d[3];
	
	int ss1 = int(s1)-48;
	int ss2 = int(s2)-48;
	int dd1 = int(d1)-48;
	int dd2 = int(d2)-48;
	
	Node src = {ss1, ss2};
 
	
	Node dest = {dd1, dd2};
 
	cout << BFS(src, dest) << endl;
return 0;
}