


func myAtoi(s string) int {
    const (
    sp = ' '
    cp = '+'
    cm = '-'
    cs = '.'
    
)
    bignum_p := big.NewInt(int64(math.Pow(float64(2),float64(31))) - 1)
    bignum_n := big.NewInt(int64(math.Pow(float64(2),float64(31))) * -1)
    r := []rune(s)
    res := []rune{}
    for _, c := range r {
        if unicode.IsDigit(c) == true {
            res = append(res, c)
            continue
        }
        if c == sp && len(res) == 0 {
            continue
        }
        if c == sp && len(res) > 0 {
            break
        }
        if c == cp && len(res) == 0 {
            res = append(res, c)
            continue
        }
        if c == cp && len(res) > 0 {
            break
        }
        if c == cm && len(res) == 0 {
            res = append(res, c)
            continue
        }
        if c == cm && len(res) > 0 {
            break
        }
        if unicode.IsLetter(c) == true {
            break
        }
        if c == cs {
            break
        }
    }
    fmt.Println(string(res))
	value := big.NewInt(0)
	_, err := value.SetString(string(res), 10);
    //value, err := strconv.ParseInt(string(res), 10, 64)
    if err != true {
        return 0
    }
    if value.Cmp(bignum_n) == -1 {
        return int(bignum_n.Int64())
    }
    if value.Cmp(bignum_p) == 1 {
        return int(bignum_p.Int64())
    }
    return int(value.Int64())
    
}