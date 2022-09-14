class Cars:
    __cars__=0
    def __init__(self,model,brand,year,km):
        self.model=model
        self.brand=brand
        self.realized_year=year
        self.km=km
        self.__cars__+=1
    def __repr__(self):
        print(f'{self.model}{self.brand}')
    def __eq__(self,y ) :
        return self.km==y.km
    def __lt__(self,y):
        return self.km<y.km
    def __le__(self,y):
        return self.km<=y.km




auto=Cars('Genesis','Hyndai',2018,2000)
auto.__repr__()

auto2=Cars('K4','KIA',2015,4000)