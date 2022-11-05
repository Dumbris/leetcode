package main
func maxArea(height []int) int {
    var i, j int = 0, len(height)-1
    var volume_max int = 0
    var volume int = 0
    var min_heigh = 0
    for i < len(height) && i < j {
        if height[i] < height[j] {
            min_heigh = height[i]
        } else {
            min_heigh = height[j]
        }
        volume = min_heigh * (j - i)
        if volume_max < volume {
            volume_max = volume
        }
        //fmt.Println("i j volume volume_max", i,j, volume, volume_max)
        if ((height[i+1] >= height[i]) || (height[i+1] < height[j])) && (height[i] < height[j]) {
            i++
            continue
        }
        j--
        
    }
    return volume_max
}