import lal



# ANDERSON CHUNK:

# “Here we loosen the definition of a chunk and consider any base-level
# subtree a possible chunk defined by the following criteria: (i) the components
# of a chunk are syntactically linked; (ii) there is only one level of dependency
# (one head and its dependents); (iii) the components are continuous; and (iv) no
# dependent within a chunk has a dependent outside the chunk.”


class Chunker:

    def __init__(self, sentence, chunk_type = "macutek"):
        self.sentence = sentence
        self.chunks = {}
        self.chunk_edges = {}
        self.chunk_index = {}
        if chunk_type.lower() == "macutek":
            self.run_macutek()
        elif chunk_type.lower() == "anderson":
            pass
        else:
            print("Unsupported chunk type! Try \"Macutek\" or \"Anderson\"")

    def run_macutek(self):
        '''
        MACUTEK CHUNK: Linear dependency segment definition

        We define the linear dependency segment (LDS henceforward) as the longest possible sequence of
        words (belonging to the same clause) in which all linear neighbours (i.e. words adjacent in a sentence)
        are also syntactic neighbours (i.e. they are connected by an edge in the syntactic dependency tree which
        represents the sentence)
        '''
        chunk = 1
        for word, parent in enumerate(self.sentence, 1):
            # initialize new chunk
            if self.chunks.get(chunk) is None:
                self.chunks[chunk] = set()

            next_is_child, next_is_parent = False, False

            if word + 1 <= len(self.sentence):
                # is next word the parent of the current?
                if parent == word + 1:
                    self.chunks[chunk].update([word, parent])
                    next_is_parent = True

                # is the current word parent of the next?
                if self.sentence[word] == word: # because of the different indexings, this is "word + 1" in zero-indexing
                    self.chunks[chunk].update([word, word+1])
                    next_is_child = True

            # break chunk if the next word is not syntactically related
            if not (next_is_parent or next_is_child):
                chunk += 1

        self._populate_chunk_index()
        self._chunk_edges()

    def _chunk_edges(self):
        for chunk_id, chunk in self.chunks.items():

            for word in chunk:
                parent = self.sentence[word-1]  # remember the 0-indexing
                parent_chunk = self.chunk_index[parent]
                if parent not in chunk:
                    self.chunk_edges[chunk_id] = parent_chunk

    def _populate_chunk_index(self):
        for chunk_id, chunk in self.chunks.items():
            for word in chunk:
                self.chunk_index[word] = chunk_id
        self.chunk_index[0] = 0  # root chunk


sentence = [3, 1, 0, 3, 6, 4, 6]
chunker = Chunker(sentence)
print(chunker.chunks)
print(chunker.chunk_edges)


# for debugging:
# print("current word: " + str(word))
# print("next word: " + str(word + 1))
# print("current parent: " + str(parent))
# try:
#     print("next parent: " + str(sentence[word]))
# except:
#     pass
# print()
# print()
