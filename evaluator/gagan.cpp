//graph representation using complex list
#include<bits/stdc++.h>
#include<ctime>
using namespace std;

struct Node
{
    struct OutgoingLink
    {
        Node *to;
        int weight;
    };
    struct IncomingLink
    {
        Node *from;
        int weight;
    };

    int value;
    vector<OutgoingLink> outgoing_links;
    vector<IncomingLink> incoming_links;

};
int main()
{
    map<int,struct Node*> m;
    int isTime;
    cin >> isTime;
    size_t s;
    clock_t start,end;
    start = clock();
    while(1)
    {
        int v1,v2,weight;
        cin >> v1;
        if(v1<0)
        {
            break;
        }
        cin >> v2;
        cin >> weight;
        struct Node* node1 = NULL;
        struct Node* node2 = NULL;
        if(m.find(v1)!=m.end())
        {
            node1 = m[v1];
        }
        if(m.find(v2)!=m.end())
        {
            node2 = m[v2];
        }
        if(node1==NULL)
        {
            node1 = new Node;
	           s += sizeof(Node);
            node1->value = v1;
            m[v1] = node1;
        }
        if(node2==NULL)
        {
            node2 = new Node;
            s += sizeof(Node);
            node2->value = v2;
            m[v2] = node2;
        }
        Node::OutgoingLink ol;
        Node::IncomingLink il;
        il.from = node1;
        ol.to = node2;
        il.weight = weight;
        ol.weight = weight;
        (node1->outgoing_links).push_back(ol);
        (node2->incoming_links).push_back(il);
    }
    end = clock();
    clock_t time = (end - start );
	if(!isTime)
    		cout << s / 8<< endl;
	else
		cout << time << endl;

    map<int,Node*>::iterator it;
    for(it = m.begin();it!=m.end();it++)
    {
        Node* temp = it->second;
        int l1 = temp->incoming_links.size();
        int l2 = temp->outgoing_links.size();
        //cout << "Vertex:" << temp->value << "\n";
        //cout << "Incoming edge weights \n";
        int i;
        /*
        for(i=0;i<l1;i++)
        {
            cout << temp->incoming_links[i].weight << " " ;
        }
        //cout << "\n";
        //cout << "Outgoing edge weights \n";
        for(i=0;i<l2;i++)
        {
            cout << temp->outgoing_links[i].weight << " " ;
        }
        cout << "\n";
	*/
    }
}
