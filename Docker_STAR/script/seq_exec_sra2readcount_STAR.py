import os

is_sra = 'yes'
is_paired = 'yes'
is_qualitycheck = 'yes'
is_delete_FASTQ = 'no'
thread_num = 12 # thread number
species = 'TAIR10'
annotation_file = species+'.gff3'
annotation = os.path.join('/condir',annotation_file)
STARidx_dir = '/condir'

root_dir = '/condir/'
input_dir = os.path.join(root_dir,'input')
output_dir = os.path.join(root_dir,'output')

fr = open(os.path.join(root_dir,'fastq_files.txt'),'r').readlines()
for line in fr:
    line = line.replace('\n','')
    lst = line.split(',')
    filename = lst[0]
    samplename = filename
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    msg = '%s is now processing...' % (samplename)
    print( msg )
    cmd = 'python exec_sra2readcount_STAR.py %s %s %s %s %d %s %s %s %s %s %s' % (is_sra,is_paired,is_qualitycheck,is_delete_FASTQ,thread_num,samplename,species,annotation,input_dir,output_dir,STARidx_dir)
    print( cmd )
    os.system(cmd)

