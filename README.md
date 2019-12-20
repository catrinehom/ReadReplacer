# ReadReplacer

ReadReplacer is a pipeline to replace a subset of reads in a fastq file. 
This is useful when e.g. having made high-accuracy basecalling on a subset of reads, and want to replace those in the original full fastq file. 


## Requirements of fastq files
This pipeline only works if the text after '@' and before a whitespace is unique for each read, since the replacement is based on that. E.g. for the read ID below:

@c67eff07-d8f3-46ef-9464-fb18747d8cce runid=b4155af00e8e925ee5548212b47fe1ab8282c463 read=51 ch=78 start_time=2019-10-03T12:56:22Z flow_cell_id=AAN745 protocol_group_id=run55 sample_id=run55

'c67eff07-d8f3-46ef-9464-fb18747d8cce' is the unique identifyer.

## Installation

The following instructions will install the latest version of ReadReplacer:

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

