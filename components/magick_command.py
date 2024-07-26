import subprocess

class Magick:
    @staticmethod
    def run_magick_command(command, is_print=True):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            if is_print:
                print(f"Error: {result.stderr.decode('utf-8')}")
            raise Exception(f"Error: {result.stderr.decode('utf-8')}")
        else:
            if is_print:
                print(result.stdout.decode('utf-8'))

    @staticmethod
    def is_magick_installed():
        try:
            Magick.run_magick_command(command = "magick -version", is_print=False)
            return True
        except Exception as e:
            return False