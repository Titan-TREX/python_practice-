# class open_File:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()

# with open_File('example.txt', 'w') as f:
#     f.write('Hello, World!')




from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with open_file('example2.txt', 'w') as f:    
    f.write('Hello, World!')