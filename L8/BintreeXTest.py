import L8_Bintree_X

tree = L8_Bintree_X.Bintree()

tree.put(7);
tree.put(8);
tree.put(0);
tree.put(3);
tree.put(1);
tree.put(10);
tree.put(9);
tree.put(4);
tree.printtree();

tree.remove(9);
tree.printtree();

tree.remove(8);
tree.printtree();

tree.remove(3);
tree.printtree();

tree.remove(7);
tree.printtree();

tree.remove(4);
tree.printtree();

tree.remove(10);
tree.printtree();

tree.remove(1);
tree.printtree();

tree.remove(0);
tree.printtree();

tree.remove(0);
tree.printtree();
