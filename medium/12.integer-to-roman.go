package main
func intToRoman(num int) string {
    var buffer bytes.Buffer
    m := map[int]string{1000:"M",
                        900:"CM",
                        500:"D",
                        400:"CD",
                        100:"C",
                        90:"XC",
                        50:"L", 
                        40:"XL",
                        10:"X",
                        9:"IX",
                        5:"V", 
                        4:"IV",
                        1:"I"}
    keys := []int{1000,900,500,400,100,90,50,40,10,9,5,4,1}
    for num > 0 {
        //fmt.Println(num)
        for _, denominator := range keys {
            letter := m[denominator] 
            quotient, remainder := num/denominator, num%denominator
            //fmt.Println(quotient, remainder, denominator, letter, buffer.String())
            if quotient > 0 {
                for i := quotient; i > 0; i-- {
                    buffer.WriteString(letter)        
                }
                num = remainder
                break
            }
            
        }
    }

    return buffer.String()
}