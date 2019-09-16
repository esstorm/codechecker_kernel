from ipykernel.kernelbase import Kernel
from subprocess import Popen, PIPE, call, CalledProcessError

class EchoKernel(Kernel):
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
            runCmd = 'echo "{code}" > tmp/file.cc && ./cc_wrapper tmp/file.cc'.format(code=code);
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
