#include<bits/stdc++.h>
using namespace std;
struct Edge
{
	int v1;
	int v2;
	float weight;
};
struct Graph
{
	vector<struct Edge> EdgeList;
	int type;
};
void printIncidence(struct Graph G)
{
	vector<vector<int> > Incidence;
	int E = G.EdgeList.size();
	set<int> vertices;
	for(int i = 0; i < E; i ++ )
	{
		vertices.insert(G.EdgeList[i].v1);
		vertices.insert(G.EdgeList[i].v2);	
	}
	int V =vertices.size();
	set<int> ::iterator it;
	it =vertices.begin();
	map<int,int> indices;
	int i= 0;
	printf("%2d ",0);
	for(it = vertices.begin(); it != vertices.end(); it ++)
	{
		indices[*it] = i;
		printf("%2d ",*it);
		i ++;
	}
	cout << endl;	
	for(int i = 0; i < E; i ++ )
	{
		vector<int> b(V);
		int v1 = indices[G.EdgeList[i].v1];
		int v2 = indices[G.EdgeList[i].v2];
		b[v2] = 1 -(2*G.type);
		b[v1] = 1;
		Incidence.push_back(b);	
	}
	for(int i = 0; i < E;i++)
	{
		printf("%2d ",i+1);
		for(int j = 0; j < V; j ++ )
			printf("%2d ",Incidence[i][j]);

		cout << endl;
	}
	
}
void printProperties(struct Graph G)
{
	cout << "Properties of the Graph are:" << endl;
	if(G.type == 0)
		cout << "Undirected\n";
	if(G.type == 1)
		cout << "Directed\n";
	bool weighted = false;
	set<int> weights;
	for(int i = 0; i < G.EdgeList.size(); i ++)
	{
		weights.insert(G.EdgeList[i].weight);
		if(weights.size() > 1)
		{
			weighted = true;
			break;
		}
	}
	if(weighted)
		cout << "Weighted\n";
	else
		cout << "Unweighted\n";
	bool simple = true;
	bool selfloop = false;
	bool parrallelEdges = false;
	set<pair<int,int> > Edges;
	for(int i = 0; i < G.EdgeList.size(); i ++ )
	{
		if(G.EdgeList[i].v1 == G.EdgeList[i].v2)
		{
			selfloop = true;
		}

	}
	for(int i = 0; i < G.EdgeList.size(); i ++ )
	{
		pair<int,int> edge = make_pair(G.EdgeList[i].v1,G.EdgeList[i].v2);
		pair<int,int> edge2 = make_pair(G.EdgeList[i].v2,G.EdgeList[i].v1);
		if(Edges.find(edge) != Edges.end())
		{
			parrallelEdges = true;
			break;
		}
		else
		{
			Edges.insert(edge);
		}
		if(G.type == 0)
		{
			if(Edges.find(edge2) != Edges.end())
			{
				parrallelEdges = true;
				break;
			}
			else
			{
				Edges.insert(edge2);
			}
		}
	}
	if(selfloop)
		cout << "Contains Self Loop" << endl;
	else
		cout << "Doesn't contain Self Loop" << endl;
	if(parrallelEdges)
		cout << "Contains Parrallel Edges" << endl;
	else
		cout << "Doesn't contain Parrallel Edges" << endl;
	if(!selfloop and !parrallelEdges)
		cout << "Simple Graph" << endl;
	else
		cout << "Not a Simple Graph" << endl;
}
int main()
{
		struct Graph G;
		cout << "Enter 1 for directed and 0 for undirected\n";
		int dir;
		cin >> dir;
		G.type = dir;
		cout << "Enter the edges in this order : Start , End, Weight ( Enter - 1 if you want to stop):\n";
		while(1)
		{
			int v1,v2;
			float w;
			cin >> v1;
			if(v1 == -1)
			 	break;
			cin >> v2 >> w;
			struct Edge e;
			e.v1 = v1;
			e.v2 = v2;
			e.weight = w;
			G.EdgeList.push_back(e);
		}
		printProperties(G);
		printIncidence(G);
}
