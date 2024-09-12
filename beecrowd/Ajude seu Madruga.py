def area_cima(corte, tiras):
    area = 0
    for x in tiras:
        if x>corte:
            area += x - corte
    return area
        
def area_total(tiras):
    area = 0
    for x in tiras:
        area += x
    return area

def achar_corte(tiras, area, baixo, cima):
    while abs(baixo - cima) > 0.0001:
        tramontina = round((baixo+cima)/2, 4)
        tlvz_area = round(area_cima(tramontina, tiras), 4)
        if abs(area - tlvz_area) < 0.001:
            return tramontina
        elif tlvz_area < area:
            return achar_corte(tiras, area, round(tramontina+0.001, 4), cima)
        else:
            return achar_corte(tiras, area, baixo, round(tramontina-0.001, 4))
    return 0

quantiras, area = map(int, input().split())
while True:
    if quantiras == area == 0:
        break
    tiras = list(map(int, input().split()))
    if area > area_total(tiras):
        print("-.-")
        quantiras, area = map(int, input().split())
        continue

    tiras = sorted(tiras)[::-1]
    corte = achar_corte(tiras, area, 0, tiras[0])
    if corte == 0:
        print(":D")
    else:
        print(f"{corte:.4f}")
    
    quantiras, area = map(int, input().split())