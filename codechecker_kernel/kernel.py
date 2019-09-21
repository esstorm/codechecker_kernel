from ipykernel.kernelbase import Kernel
from subprocess import Popen, PIPE, call, CalledProcessError
import re

class CCKernel(Kernel):
    implementation = 'CodeChecker'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'name': 'c++',
                    'codemirror_mode': 'text/x-c++src',
                    'mimetype': ' text/x-c++src',
                    'file_extension': '.cc'
    }
    banner = "Analyze c/c++ code inside Jupyter notebooks using Clang SA"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            with open("/tmp/file.cc", "w") as tmpFile:
                tmpFile.write(code)
            runCmd = """clang --version | head -1
                        CodeChecker check --print-steps -b "clang -c /tmp/file.cc" \
                        | grep -v '\[INFO' \
                        | sed -e '/----==== Summary ====----/,$ d'
            """
            proc = Popen([runCmd], stdout=PIPE, shell=True)
            res, _ = proc.communicate()

            stream_content = {'name': 'stdout', 'text': res}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
