def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    #input_string = input("enter string")
    input_string = "chbvjrxwppkbrqdcxcsswvarrxyxunusswxrrtemtmdlutzsjbvcnrhqxjkkxnkcfojsnpzioxtpkooybbksvnqpjkpomysfrfnepxkkmkhgwmxcgbgitrggmccurctbdrslkgaaaxfnvqzdxmkassmxihvjktswbgeoegrxemomxqyicgfyelxphelkvsatkhcwshqiaepyzctzbplcmaqrjvqlfaifmjurpuoreivpzusdefcknlteyqfbervigtvuwtwjaepkudrbzpnguqtkzeitpvgioaiwyjxavwxiewxldzmuamcwibudvrylrjrzxnoddduzyxthirsevuwngigcghbctzrnmairvtiupmoaykcqeqwdzuaeerafrderfenulodiublpejlwfapvskjkxtuylotldfanewqrozgvcwcwoeihvutgbamghcchmdgrkawmpqlrffibxxaswszvxhxidzezxqorpvseyokpcxouwttdekpgxqqklekangvhexrjtyyhfmwttqmaccczrrekmnnnmnuztgbgagggbgbikpcnkovffqhhguuqhcuyjosbftxnkzirlmadrwbjlqezyabdscixisgbyfwptcglzcxsxhxarnakofxavtfchscnpkneageuefoiiccojfewpmixbzjaawjzsvmmzltktdmfmdnzdbhafdmeydzmfhyuhgazgvsepvowxeakjecnocqhileaooammqxlngxdglrwtwmkauszkmtchbnfzbzmghssyzldochzmxqdqxqcwvgnpafoxujhhriznmopsopfwblycetggbmwrkzhsqjrnpmdtnybbjmcifsybvjkhnjndtmztnzfodvhcjmavervwbodvcbyibpgiyeemveqimejksrzhtladheckrqofnpwotufmqrwzaigtpfkpopfmumctpbjigfcuxppbvxcbtncfhyghwoldutjanpsdholekci"

    def reverse_string(input_string):
        print(len(input_string))
        #print("input str", input_string)
        if (len(input_string) == 0):
            return input_string
        else:
            print(input_string[1:], input_string[0])
            return reverse_string(input_string[1:]) + input_string[0]
    print(reverse_string(input_string))

if __name__ == '__main__':
    main()