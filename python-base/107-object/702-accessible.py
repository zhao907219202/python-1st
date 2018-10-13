class Secretive:
    # 两个下划线是外界无法直接访问
    def __inaccessible(self):
        print("Bet you cannot see me")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()
# s.__inaccessible()    AttributeError: 'Secretive' object has no attribute '__inaccessible'
s.accessible()

print()
# 可以在前面加单下划线和类名进行访问（不建议）
print(Secretive._Secretive__inaccessible)
s._Secretive__inaccessible()
