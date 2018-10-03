#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
typedef struct {
    unsigned int first;
    unsigned int second;
} edge;

typedef void (*treefn)(const edge *, unsigned int);

/* Check if vertices v1 and v2 are in different components in the tree */
void connected_components_recursive(const edge *edges, unsigned int n,
        int *components, unsigned int order, unsigned int vertex,
        unsigned int component)
{
    unsigned int i;
    /* Put this vertex in the current component */
    components[vertex] = component;
    for (i = 0; i < n; i++) {
        if (edges[i].first == vertex || edges[i].second == vertex) {
            /* Adjacent */
            const unsigned int neighbour = edges[i].first == vertex ?
                    edges[i].second : edges[i].first;
            if (components[neighbour] == -1) {
                /* Not yet visited */
                connected_components_recursive(edges, n, components, order, neighbour, component);
            }
        }
    }
}

unsigned int connected_components(const edge *edges, unsigned int n, unsigned int order,
        int **components)
{
    unsigned int i;
    unsigned int component = 0;
    *components = (int * )malloc(order * sizeof(int));
    if (components == NULL) {
        return 0;
    }
    for (i = 0; i < order; i++) {
        (*components)[i] = -1;
    }

    for (i = 0; i < order; i++) {
        if ((*components)[i] == -1) {
            connected_components_recursive(edges, n, *components, order, i, component);
            component++;
        }
    }
    return component;
}
static unsigned int different_components(const edge *tree, unsigned int t, unsigned int order,
        unsigned int v1, unsigned int v2)
{
    int *components;
    unsigned int different;
    connected_components(tree, t, order, &components);
    different = components[v1] != components[v2];
    free(components);
    return different;
}

static void spanning_trees_recursive(const edge *edges, unsigned int n, unsigned int order,
        edge *tree, unsigned int t, int predecessor, treefn fun,int count)
{
    if (t == order - 1) {
        /* Found a tree */
        fun(tree, order - 1);
    }
    else {
        unsigned int e;
        for (e = predecessor + 1; e < n; e++) {
            if (t == 0 /* First edge */
                || different_components(tree, t, order,
                    edges[e].first, edges[e].second))
            {
                tree[t] = edges[e];
                spanning_trees_recursive(edges, n, order, tree, t + 1, e, fun,count);
            }
        }
    }
}

void spanning_trees(const edge *edges, unsigned int n, unsigned int order, treefn fun,int count)
{
    edge *tree;
    tree = (edge *)malloc((n - 1) * sizeof(edge));
    if (tree == NULL) {
        return;
    }
    spanning_trees_recursive(edges, n, order, tree, 0, -1, fun,count);
    free(tree);
}


/* Calculate the nth triangular number T(n) */
unsigned int triangular_number(unsigned int n)
{
    return (n * (n + 1)) / 2;
}

/* Construct a complete graph on v vertices */
edge *complete_graph(unsigned int v)
{
    const unsigned int n = triangular_number(v - 1);
    unsigned int i, j, k;
    edge *edges = (edge *) malloc(n * sizeof(edge));
    if (edges != NULL) {
        for (i = 0, k = 0; i < v - 1; i++) {
            for (j = i + 1; j < v; j++) {
                edges[k].first = i;
                edges[k].second = j;
                k++;
            }
        }
    }
    return edges;
}

/* Print the edges in a tree */
static void print_tree(const edge *tree, unsigned int n)
{
    unsigned int e;
    for (e = 0; e < n; e++) {
        printf("(%u, %u) ", tree[e].first, tree[e].second);
    }
    putchar('\n');
}


int main(void)
{
    printf("Enter the number of Vertices\n");
    int k;
    scanf("%d",&k);

    const unsigned int n = k;
    edge *edges;
    edges = complete_graph(n);
    //edges = (edge *) malloc(n * sizeof(edge));
    if (edges == NULL) {
        return 1;
    }
    printf("Input the edges:\n");
    int i = 0;
    int first,second;
    for ( i = 0; i < n ; i ++ )
    {
      scanf("%d%d",&first,&second);
      edges[i].first = first;
      edges[i].second = second;
    }
    spanning_trees(edges, n, v, print_tree,0);
    free(edges);

    return 0;
}
