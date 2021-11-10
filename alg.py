class Alg:
    def __init__(self, graph):
        self.graph = graph

    def search_min(self, tr, vizited):
        m = 32767
        for ind in vizited:
            for index, elem in enumerate(tr[ind]):
                if elem < m and index not in vizited:
                    m = elem
                    i1 = index
                    i2 = ind
        return [m, i1, i2]

    def prim(self):
        result = [[] for i in range(0, self.graph.size)]
        to_visit = [i for i in range(1, self.graph.size)]
        vizited = [0]
        weight = 0
        for index in to_visit:
            w, i1, i2 = self.search_min(self.graph.points, vizited)
            print(w, i1, i2)
            weight += w
            result[i1].append(i2+1)
            result[i2].append(i1+1)
            vizited.append(i1)
            print(vizited)
        return [result, weight]

    def print_results(self):
        f = open("out.txt", "a")
        skeleton, w = self.prim()
        for i in range(len(skeleton)):
            for v in sorted(skeleton[i]):
                f.write(str(v) + ' ')
            f.write('0\n')
        f.write(str(w) + '\n')
        f.close()
