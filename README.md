# ReadReplacer

ReadReplacer is a pipeline to replace a subset of reads in a fastq file. 
This is useful when e.g. having made high-accuracy basecalling on a subset of reads, and want to replace those in the original full fastq file. 


## Installation

The following instructions will install the latest version of ContigExtractor:

```
git clone https://github.com/catrinehom/ReadReplacer.git

cd ReadReplacer/
chmod a+x ReadReplacer.py
```

### Move to bin 
You might want to move the program to your bin to make the program globally excecutable. 
The placement of your bin depends on your system configuration, but common paths are:

```
/usr/local/bin/
```
OR
```
~/bin/
```

Example of move to bin:

```
mv ReadReplacer.py /usr/local/bin/
```

## Usage

To run full pipeline:

```
./ReadReplacer.py [-a <fastq filename (all reads)>] [-q <fastq filename (reads to replace)>] [-o <output filename>]
```

