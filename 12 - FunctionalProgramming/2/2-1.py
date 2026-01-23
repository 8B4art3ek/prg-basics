# Kurs edukacyjny kończy się testem sprawdzającym wiedzę uczestników. Aby zaliczyć kurs, uczestnik musi uzyskać minimalną liczbę punktów. Poniższy program zawiera funkcję wyższego rzędu min_pts, która zwraca inną funkcję. Przeczytaj kod programu. Następnie uruchom program.

def min_pts(limit):
    def check(pts):
        if pts >= limit:
            return True
        return False
    return check

print("=== MIN 50 PTS TO PASS ===")
assess_test = min_pts(50)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")

print("=== MIN 60 PTS TO PASS ===")
assess_test = min_pts(60)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")