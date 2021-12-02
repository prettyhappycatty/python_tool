
import sys
import os

## atcoderのtestデータを、テキストファイルに出力する
## usage: python atcoder_test_folder_to_text.py {folder_path} {output_text_name}
def main():
    args = sys.argv

    path = args[1]
    output_file_name = args[2]

    files = os.listdir(path+'/in/')
    files.sort()
    print(files)

    with open(path+output_file_name, mode='w') as f:
        f.write(path+ "\r\n")
        for n in files:
            f.write(n+ "\r\n")
            with open(path+'/in/'+n) as in_f:
                s = in_f.read()
                f.write("  in："+s)
            with open(path+'/out/'+n) as out_f:
                s = out_f.read()
                f.write("  out:"+s)

if __name__ == "__main__":
    # execute only if run as a script
    main()


