package main
import "fmt"

func arr2map(nums []int) map[int]int {
    res := map[int]int{}
    for _, v := range nums {
        if _, ok := res[v]; ok {
            res[v]++
        } else {
            res[v] = 1
        }    
    }
    return res
}

func sort3(a,b,c int) [3]int {
    var el [3]int
    if a <= b && b <= c { 
        el = [3]int{a,b,c} 
    } else if a <= c && c <= b { 
        el = [3]int{a,c,b} 
    } else if b <= a && a <= c { 
        el = [3]int{b,a,c}  
    } else if c <= a && a <= b { 
        el = [3]int{c,a,b}
    } else if c <= b && b <= a { 
        el = [3]int{c,b,a}
    } else if b <= c && c <= a { 
        el = [3]int{b,c,a}                        
    } else { 
        fmt.Println("Too far away.", a,b,c) 
    }
    //fmt.Println("%v", el)
    return el
}

func unique(el [3]int, res *[][3]int, res2 *[][]int) bool {
    add := true
    for _,el2 := range *res {
        if el2 == el {
            add = false
        }
    }
    if add {
        *res = append(*res, el)
        *res2 = append(*res2, el[:])
    }                   
    return add
}

func threeSum(nums []int) [][]int {
    if len(nums) < 3 {
        return [][]int{}
    }
    res := make([][3]int, 0)
    res2 := make([][]int, 0)
    m := arr2map(nums)
    //fmt.Println("%v", m)
    for k,_ := range m {
        for k2,_ := range m {
            if _, ok := m[-1*(k+k2)]; ok {  
                m[k]--
                m[k2]--
                m[-1*(k+k2)]--
                if m[k] >= 0 && m[k2] >= 0 && m[-1*(k+k2)] >= 0  {
                    unique(sort3(k,k2,-1*(k+k2)), &res, &res2)
                }
                m[k]++
                m[k2]++
                m[-1*(k+k2)]++
            }
            
        }
        
    }
    return res2
}
