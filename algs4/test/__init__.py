"""
Week 1 tests.

Test cases reside inside union_find_test.py.
Literals and methods SPECIFIC for union_find.py used in tests are in union_find_fixture.py
Methods which can be in time promoted to common are inside utils.py

There is also an integration test with reference Java implementation - test_results_with_output_of_java_implementation.
Java output was generated with WeightedQuickUnionUF class for every input.
Mentioned input files are inside input directory (.txt extension was changed to .in) and are downloaded from course's
website:

- https://algs4.cs.princeton.edu/15uf/tinyUF.txt
- https://algs4.cs.princeton.edu/15uf/mediumUF.txt
- https://algs4.cs.princeton.edu/15uf/largeUF.txt

Main of the Java class which was generating output:

public static void main(String[] args) {
    int n = StdIn.readInt();
    WeightedQuickUnionUF uf = new WeightedQuickUnionUF(n);
    while (!StdIn.isEmpty()) {
        int p = StdIn.readInt();
        int q = StdIn.readInt();
        if (uf.connected(p, q)) continue;
        uf.union(p, q);
        StdOut.println(Math.min(p,q) + " " + Math.max(p,q)); // To account for symmetric property of a connection
                                                             // (same result for union(p, q) and union(q, p)).
    }
    StdOut.println(uf.count() + " components");
}
"""

REFERENCE_OUTPUT_DIR = 'reference'
INPUT_DIR = 'input'
