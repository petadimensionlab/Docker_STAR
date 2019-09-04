import os
import glob

## configuration ##
species_list = ['hg38','mm10','TAIR10']
species = species_list[2]

root_dir = os.getcwd()
STARidx_dir =  os.path.join('/condir/'+species)
genome_dir = '/condir/'

if not os.path.exists(STARidx_dir):
	cmd = 'mkdir %s' % (STARidx_dir)
	os.system(cmd)

## options ##
thread_num = 12
genomeFastaFile = os.path.join(genome_dir,species+'.fa')
runMode = 'genomeGenerate'
sjdbGTFfile = os.path.join('/condir',species+'.gff3') 
sjdbOverhang = str(100)


## build index ##
cmd = 'STAR --runThreadN %s --runMode %s --genomeDir %s --genomeFastaFiles %s --sjdbGTFfile %s --sjdbOverhang %s' % (int(thread_num),runMode,STARidx_dir,genomeFastaFile,sjdbGTFfile,sjdbOverhang)
print(cmd)
os.system(cmd)

## Change the access permission ##
