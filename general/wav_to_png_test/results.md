# Hypothesis

Will the .wav file's spectogram be larger in size? The wave is split into several smaller ones (by time), then FFT is applied. The pieces' spectograms are "concatenated". Shouldn't the spectogram file size be larger, than the original?


# Results of testing

For several .wav files were built their spectograms and saved into .png.
The sizes of the files are then compared.

| filename | .wav size | .png size | wav / png % (more is better) |
|  :----:  |   :----:  |   :----:  |        :----:      |
| cat_y    | 49060     | 91880     | 53.4               |
| eleph    | 2646044   | 2678776   | 98.8               |
| hyena    | 146942    | 154721    | 95.0               |