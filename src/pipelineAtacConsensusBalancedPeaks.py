import os

# Based on /home/mbp15ja/dev/pipeline_atacseq/src/pipelineAtacseq.virtualSEConditionPooling
# Creates a statement to concatenate the contents of all the files into the corresponding output file.
#
# Inputs:
#     
#     -input_files: The input files to concatenate
#     -output_file: Output file containing a concatenation of all the 
#            single end input_files. 
#
# Outputs:
#     -returns the statement to concatenate the contents of the files.
def SEPooling(input_files, output_file):
    
    # Begin the construct of the statements
    statement = '''zcat '''
    
    
    # Go through the array of samples, get the sample type and create the statements
    for sample in input_files:
    
        # Add the sample_name 
        statement += (sample + " ")  
    
    # Add the final command to each statement
    statement += ''' | gzip -c > '''+output_file
    
    return statement