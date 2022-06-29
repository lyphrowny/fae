import getopt
from pathlib import Path
import sys

import matplotlib.pyplot as plt
from scipy.io import wavfile


def _parse_args(args):
    w_fn, i_fn, i_dest = "", "", ""
    help_msg = "wav_to_pngspectr.py -w <input>.wav [,-d <dest_dir>, -i <output>.png]"
    try:
        opts, args = getopt.getopt(args, "hw:i:d:", ["wav_fn=", "im_fn=", "i_dest="])
    except getopt.GetoptError:
        print(help_msg)
    for opt, arg in opts:
        if opt == "-h":
            print(help_msg)
            exit(0)
        elif opt in ("-w", "--wav_fn"):
            w_fn = Path(arg).with_suffix(".wav")
        elif opt in ("-i", "--im_fn"):
            i_fn = Path(arg).with_suffix(".png")
        elif opt in ("-d", "--i_dest"):
            i_dest = Path(arg)

    if not w_fn:
        print("The .wav filename should be specified")
    if not i_fn:
        i_fn = w_fn.with_suffix(".png")
    if i_dest:
        i_fn = i_dest.joinpath(i_fn.name)
    return w_fn, i_fn


def _wav_2_png(w_fn, i_fn):
    s_freq, s_data = wavfile.read(w_fn)
    *_, spec = plt.specgram(s_data, Fs=s_freq)
    spec.write_png(i_fn)


def _get_file_sizes(filenames):
    for fn in filenames:
        print(f"{fn} size: {fn.stat().st_size} bytes")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("At least the .wav filename is needed as argument")
    w_fn, i_fn = _parse_args(sys.argv[1:])
    _wav_2_png(w_fn, i_fn)
    _get_file_sizes((w_fn, i_fn))