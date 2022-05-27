func romanToInt(s string) int {
    var res int = 0
    m := map[string]int{"M":1000,
                        "CM":900,
                        "D":500,
                        "CD":400,
                        "C":100,
                        "XC":90,
                        "L":50, 
                        "XL":40,
                        "X":10,
                        "IX":9,
                        "V":5, 
                        "IV":4,
                        "I":1}
    keys := []string{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"}
    for len(s) > 0 {
        for _,k := range keys {
            if strings.HasPrefix(s, k) {
                res = res + m[k]
                s = strings.TrimPrefix(s, k)
                break
            }
            
        }
        
    }
    
	return res
}