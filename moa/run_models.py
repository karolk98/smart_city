import os

data_path = "DataSet/ztm5_2/"


dump_path = "../results/"

datasets = [
    # 'abr50',
    # 'abr500',
    # 'abr5000',
    # 'inc50',
    # 'inc500',
    # 'inc5000',
    # 'no50',
    # 'no500',
    # 'no5000',
    # 'reo50',
    # 'reo500',
    # 'reo5000'
# 'abr',
# 'alt',
# 'hist-alt',
# 'hist-seq-ind',#tu
# 'hist-seq',
'hist-tar',
# 'long-hist-seq',
# 'long-seq',
# 'seq-ind',
# 'seq',
# 'tar',
# 'tar-ind',
# 'hist-tar-ind'#tu
]

for dataset in datasets:
    print(os.path.exists(f'{data_path}{dataset}.arff'))

model_dict = {
    "maj": "functions.MajorityClass",
    "bayes": "bayes.NaiveBayes",
    "hat": "trees.HoeffdingAdaptiveTree",
    "knn": "lazy.kNN",
    "perceptron": "functions.Perceptron",
    "SGD": "functions.SGD",
    "levbag": "meta.LeveragingBag",
    "arf": "meta.AdaptiveRandomForest",
    "srp": "meta.StreamingRandomPatches",
    "melanie-boost": "\(meta.Melanie -b meta.OzaBoost\)",
    "melanie": "meta.Melanie",
    "melanie2": "meta.Melanie2",
    "smelanie": "meta.Smelanie",
    "MARLINE": "marline.MSBC",
    "blast": "meta.Blast2",
}

models = [
    "maj",
    # "bayes",
    # "hat",
    # "knn",
    # "perceptron",
    # "SGD",
    # "levbag",
    # "arf",
    # "srp",
    # "melanie-boost",
    # "melanie",
    # "melanie2",
    # "smelanie",
    # "MARLINE",
    # "blast"
]

bs = '/Users/karol/Library/Java/JavaVirtualMachines/openjdk-18.0.1.1/Contents/Home/bin/java -javaagent:sizeofag-1.0.4.jar -javaagent:"/Applications/IntelliJ IDEA CE.app/Contents/lib/idea_rt.jar=53508:/Applications/IntelliJ IDEA CE.app/Contents/bin" -Dfile.encoding=UTF-8 -classpath /Users/karol/Desktop/masters/moa-18.06.0/moa/target/classes:/Users/karol/.m2/repository/nz/ac/waikato/cms/weka/weka-dev/3.9.2/weka-dev-3.9.2.jar:/Users/karol/.m2/repository/nz/ac/waikato/cms/weka/thirdparty/java-cup-11b/2015.03.26/java-cup-11b-2015.03.26.jar:/Users/karol/.m2/repository/nz/ac/waikato/cms/weka/thirdparty/java-cup-11b-runtime/2015.03.26/java-cup-11b-runtime-2015.03.26.jar:/Users/karol/.m2/repository/nz/ac/waikato/cms/weka/thirdparty/bounce/0.18/bounce-0.18.jar:/Users/karol/.m2/repository/com/googlecode/matrix-toolkits-java/mtj/1.0.4/mtj-1.0.4.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_ref-osx-x86_64/1.1/netlib-native_ref-osx-x86_64-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/native_ref-java/1.1/native_ref-java-1.1.jar:/Users/karol/.m2/repository/com/github/fommil/jniloader/1.1/jniloader-1.1.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_ref-linux-x86_64/1.1/netlib-native_ref-linux-x86_64-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_ref-linux-i686/1.1/netlib-native_ref-linux-i686-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_ref-win-x86_64/1.1/netlib-native_ref-win-x86_64-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_ref-win-i686/1.1/netlib-native_ref-win-i686-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_ref-linux-armhf/1.1/netlib-native_ref-linux-armhf-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_system-osx-x86_64/1.1/netlib-native_system-osx-x86_64-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/native_system-java/1.1/native_system-java-1.1.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_system-linux-x86_64/1.1/netlib-native_system-linux-x86_64-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_system-linux-i686/1.1/netlib-native_system-linux-i686-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_system-linux-armhf/1.1/netlib-native_system-linux-armhf-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_system-win-x86_64/1.1/netlib-native_system-win-x86_64-1.1-natives.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/netlib-native_system-win-i686/1.1/netlib-native_system-win-i686-1.1-natives.jar:/Users/karol/.m2/repository/net/sourceforge/f2j/arpack_combined_all/0.1/arpack_combined_all-0.1.jar:/Users/karol/.m2/repository/com/googlecode/netlib-java/netlib-java/1.1/netlib-java-1.1.jar:/Users/karol/.m2/repository/com/github/fommil/netlib/core/1.1/core-1.1.jar:/Users/karol/.m2/repository/com/github/fracpete/sizeofag/1.0.4/sizeofag-1.0.4.jar:/Users/karol/.m2/repository/com/github/waikato/jclasslocator/0.0.12/jclasslocator-0.0.12.jar:/Users/karol/.m2/repository/net/sf/meka/meka/1.9.2/meka-1.9.2.jar:/Users/karol/.m2/repository/com/jidesoft/jide-oss/3.6.18/jide-oss-3.6.18.jar:/Users/karol/.m2/repository/com/github/fracpete/jfilechooser-bookmarks/0.1.6/jfilechooser-bookmarks-0.1.6.jar:/Users/karol/.m2/repository/com/github/fracpete/jclipboardhelper/0.1.1/jclipboardhelper-0.1.1.jar:/Users/karol/.m2/repository/gov/nist/math/jama/1.0.3/jama-1.0.3.jar:/Users/karol/.m2/repository/net/sf/trove4j/trove4j/3.0.3/trove4j-3.0.3.jar:/Users/karol/.m2/repository/org/kramerlab/bmad/2.4/bmad-2.4.jar:/Users/karol/.m2/repository/org/kramerlab/autoencoder/0.1/autoencoder-0.1.jar:/Users/karol/.m2/repository/org/scala-lang/scala-library/2.10.2/scala-library-2.10.2.jar:/Users/karol/.m2/repository/org/scala-lang/scala-swing/2.10.2/scala-swing-2.10.2.jar:/Users/karol/.m2/repository/org/scalatest/scalatest-maven-plugin/1.0-M2/scalatest-maven-plugin-1.0-M2.jar:/Users/karol/.m2/repository/org/apache/maven/maven-plugin-api/2.0.9/maven-plugin-api-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-project/2.0.9/maven-project-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-settings/2.0.9/maven-settings-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-profile/2.0.9/maven-profile-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-model/2.0.9/maven-model-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-artifact-manager/2.0.9/maven-artifact-manager-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-repository-metadata/2.0.9/maven-repository-metadata-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/wagon/wagon-provider-api/1.0-beta-2/wagon-provider-api-1.0-beta-2.jar:/Users/karol/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.jar:/Users/karol/.m2/repository/org/codehaus/plexus/plexus-container-default/1.0-alpha-9-stable-1/plexus-container-default-1.0-alpha-9-stable-1.jar:/Users/karol/.m2/repository/classworlds/classworlds/1.1-alpha-2/classworlds-1.1-alpha-2.jar:/Users/karol/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9/maven-reporting-api-2.0.9.jar:/Users/karol/.m2/repository/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.jar:/Users/karol/.m2/repository/org/codehaus/plexus/plexus-utils/3.0/plexus-utils-3.0.jar:/Users/karol/.m2/repository/jfree/jfreechart/1.0.13/jfreechart-1.0.13.jar:/Users/karol/.m2/repository/jfree/jcommon/1.0.16/jcommon-1.0.16.jar:/Users/karol/.m2/repository/com/googlecode/efficient-java-matrix-library/ejml/0.22/ejml-0.22.jar:/Users/karol/.m2/repository/org/markdownj/markdownj-core/0.4/markdownj-core-0.4.jar:/Users/karol/.m2/repository/com/github/fracpete/multisearch-weka-package/2017.10.1/multisearch-weka-package-2017.10.1.jar:/Users/karol/.m2/repository/org/apache/commons/commons-math3/3.6.1/commons-math3-3.6.1.jar:/Users/karol/.m2/repository/org/apache/poi/poi/3.17/poi-3.17.jar:/Users/karol/.m2/repository/commons-codec/commons-codec/1.10/commons-codec-1.10.jar:/Users/karol/.m2/repository/org/apache/commons/commons-collections4/4.1/commons-collections4-4.1.jar moa.DoTask '

# data = "DataSet/ztm5/tar.arff"
for model in models:
    print(model)
    for dataset in datasets:
        print(dataset)
        command = bs + f'EvaluatePrequential -l {model_dict[model]} -s \(ArffFileStream -f {data_path}{dataset}.arff\) -f 100 -d {dump_path}{dataset}_{model}.csv'
        os.system(command)
