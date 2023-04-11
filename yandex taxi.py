def yandex_taxi(first_3_km_sum, distance):
    if distance <= 3:
        return first_3_km_sum
    else:
        konecputi = distance - 3
        obwiycennnik = first_3_km_sum + (konecputi * 4000)
        return obwiycennnik

print(yandex_taxi(7000,5))