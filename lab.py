import sys
import lal

if len(sys.argv) != 3:
    print("Arguments needed: input_file output_file ")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print("Input file:", arg1)
print("Output file:", arg2)

tbproc = lal.io.treebank_processor()
# The object will compute all features by default
err = tbproc.init(arg1, arg2)
if err == lal.io.treebank_error_type.no_error:
    # Remove all the features
    tbproc.clear_features()
    # Now we add some metrics
    tbproc.add_feature( lal.io.treebank_feature.num_nodes )
    tbproc.add_feature( lal.io.treebank_feature.num_crossings )
    tbproc.add_feature( lal.io.treebank_feature.num_pairs_independent_edges )
    tbproc.add_feature( lal.io.treebank_feature.exp_num_crossings )
    tbproc.add_feature( lal.io.treebank_feature.predicted_num_crossings )
# Process the treebank file...
err = tbproc.process()
print(err)
