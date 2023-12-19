import numpy as np

#numpy배열 생성
#np.array(데이터 배열, 자료형, 등등)
#Vector -> 1차원 배열
#Matrix -> 2차원 배열
#Tensor -> 3차원 배열

#Vector
testarr=np.array(['1','2',3,4], np.int64)
#2차원 Matrix
testarr1=np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]], np.int64)
#3차원 Tensor
testarr2=np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                  [[9, 10, 11, 12], [13, 14, 15, 16]],
                  [[17, 18, 19, 20], [21, 22, 23, 24]]], np.int64)
print(testarr)
print(testarr1)
print(testarr2)

#ndim 차원 확인
print(testarr.ndim)
print(testarr1.ndim)
print(testarr2.ndim)

#size 크기 확인
print(testarr.size)
print(testarr1.size)
print(testarr2.size)

#type(arg): arg의 type확인
print(type(testarr))
print(type(testarr[1]))

#numpyarray.dtype -> numpy배열의 자료형(프로퍼티) 확인
print(testarr.dtype)

#numpyarray.shape -> tuple로 반환(행, 열) 1차원인 데이터의 경우 (열,)형태로 반환
print(testarr.shape)
print(testarr1.shape)
print(testarr2.shape)

#reshape함수 -> size가 동일한 범위 내에서 배열의 형태를 변환
test_reshape=np.array(([1,2,3,4],[5,6,7,8]), int)
print(test_reshape)
print(test_reshape.shape)
print(test_reshape.size)

#기존의 형태는 2, 4 즉 2 * 4 = 8 8개의 요소를 가지고 있었음
#Matrix형태를 Tensor형태로 변환
test_reshape2=test_reshape.reshape(2, 2, 2)
print(test_reshape2)
print(test_reshape2.size)

#Tensor형태를 펼침(Vector형태로 변환)
print(test_reshape2.flatten())

testindex=np.array(([1,2,3],[4,5,6]), int)
print(testindex)
#index like C
print(testindex[0][2])
print(testindex[1][1])
#another index type
testindex[0, 2] = 5
print(testindex)

testsl=np.array(([1,2,3,4],[5,6,7,8],[9,10,11,12]), int)
print(testsl)
print(testsl.shape)
print(testsl.size)
#2차원 slice
print(testsl[:,:3])

#arange == range함수와 동일. 
sp1=np.arange(40)
print(sp1)

#np.ones(채널 구성, 데이터 타입) -> numpyarray를 1로 구성한 형태로 채운다.
print(np.ones(shape=(8,), dtype=np.int64))
print(np.ones((5,2),dtype=np.int32))

#np.zeros -> 1대신 0
#정말 많이 쓴다.
print(np.zeros(shape=(8,), dtype=np.int64))
print(np.zeros((5,2),dtype=np.int32))

#np.empty -> 0로 채워진 것으로 보이지만, 형태만 선언되었고 메모리에 선언되지 않았다.
print(np.empty(shape=(8,), dtype=np.int64))
print(np.empty((5,2),dtype=np.int32))

#np.identity(정사각형 형태의 2차원배열 생성)
print(np.identity(n=5, dtype=np.int32))
#np.eye(대각선) -> 행과 열을 정해서 생성
print(np.eye(N=3, M=5, dtype=np.int64))
#k=3 -> 대각선 위치를 옮김
print(np.eye(3, 5, k=3))

#np.diag -> 대각선 추출
#k를 통해 추출하는 대각선 위치 옮기기 가능
print(np.diag(np.eye(3, 5, k=3)))
print(np.diag(np.eye(3, 5, k=3), k=3))

#np.random.uniform(low, high, n) -> low와 high 사이의 값을 균일하게 10개 생성
print(np.random.uniform(0, 1, 10))

sum = 0
arr = np.random.uniform(0, 1, 1000)
for i in range(1000):
    element=arr[i]
    sum+=element
    
print(sum/1000)

#np.random.normal(기준, 크기, 갯수) -> 정규분포 데이터를 갯수만큼 얻을 수 있다.
arr_normal=np.random.normal(0, 10, 1000)

sum=0
for i in range(1000):
    ele=arr_normal[i]
    sum+=ele
print(sum/1000)


arr_1=np.arange(1, 11)
print(arr_1)
#nparray.sum() -> 내부 데이터들을 합해 출력한다.
print(arr_1.sum())

#axis: 축
#matrix: axis=0 -> 행방향 axis=1 -> 열방향
#tensor: axis=0 -> 채널  axis=1 -> 행  axis=2 -> 열
arr_2=np.arange(1, 13).reshape(3, 4)
print(arr_2)
print(arr_2.sum(axis=0))    #행방향으로 더함
print(arr_2.sum(axis=1))    #열방향으로 더함

a=np.array([1,2,3])
b=np.array([4,5,6])

#np.vstack(a, b) -> 2개의 nparray를 세로로 합침(행추가)
print(np.vstack((a,b)))

#np.hstack(a, b) -> 2개의 nparray를 가로로 합침(열추가)
print(np.hstack((a,b)))

a=np.array([[1,2,3]])   #Matrix
b=np.array([[4,5,6]])   #Matrix

#축을 이용한 vstack, hstack의 구현
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

#concatenate 활용
a=np.array([[1,2],[3,4]])
print(a)
b=np.array([[5,6]])
print(b)
print(b.ndim)
#T -> Transpose 가로세로 변환
print(np.concatenate((a,b.T),axis=1))

#Array간 연산시 *사이즈가 같을 경우* 같은 위치에 있는 Element끼리 연산
oper_arr=np.array([1,2,3])
print(oper_arr)
print(oper_arr*oper_arr)

#array와 정수간의 연산인 경우 모든 Element에 정수와의 연산이 행해짐
broad_arr=np.array([[1,2,3],[4,5,6]])
print(broad_arr)
x=10    #스칼라: 단일값
print(broad_arr+x)
print(broad_arr-x)
print(broad_arr*x)
print(broad_arr/x)

#matrix와 vector간의 연산일 경우 같은 열 index를 가진 서로의 Data끼리 각각 연산된다.
broad_matrix=np.arange(1,13).reshape(4,3)
print(broad_matrix)
broad_vector=np.arange(10,40,10)
print(broad_vector)
print(broad_matrix+broad_vector)

#비교식도 위의 연산과 동일한 방식으로 진행된다.
comp=np.arange(10)
print(comp)
print(comp>5)
#all -> &&연산
print(np.all(comp>=0))

#np.where(조건식, 참일시 변경값, 거짓일시 변경값)
where_arr=np.arange(10)
print(where_arr)
print(np.where(where_arr>5, 0, 255))

def nans(shape, dtype=np.float64):
    a=np.empty(shape,dtype)
    #fill(arg) -> arg값으로 array를 채운다.
    a.fill(np.nan)
    return a

print(nans([3,4]))

#isnan(nparray) -> nparray에서 nan값인지 아닌지 요소마다 체크
nan_arr=np.array([1,2,3,np.nan,5])
print(np.isnan(nan_arr))
print(np.isnan(nans([3,4])))

#최대값의 행의 인덱스를 반환
arg_arr=np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18]])
print(arg_arr)
print(np.argmax(arg_arr, axis=0))   #axis=행

