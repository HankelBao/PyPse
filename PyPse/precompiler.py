class CodeLine():
    def __init__(self, file_name: str, line_num: int, content: str):
        self.file_name = file_name
        self.line_num = line_num
        self.content = content

    def get_word_by_index(self, index: int) -> str:
        return self.content.split(" ")[index]
    
    def if_include(self, exp: str) -> bool:
        if exp in self.content:
            return True
        return False

    def str_between(self, left_exp: str, right_exp: str) -> str:
        content = self.content
        return content[content.index(left_exp)+1: content.index(right_exp)]

    def split(self, exp: str) -> list:
        return self.content.split(exp)
    
    def __repr__(self):
        return f"{self.line_num}: {self.content}"

def precompile_file(f) -> list:
    file_name = f.name
    code_lines = []
    line_num = 0
    for line_str in f:
        line_num += 1
        line_str = line_str.strip("\n").strip()
        code_line = CodeLine(file_name, line_num, line_str)
        code_lines.append(code_line)
    return code_lines
