echo ""
echo ">> Tiến hành biên dịch raft lib, (Chi tiết hướng dẫn xem tại trang git của raftlib: https://github.com/RaftLib/RaftLib) "
echo ""

echo ">> Xóa thư mục [build] cũ nếu tồn tại "
echo ""

rm -r ./RaftLib/[build]

echo ">> Tạo thư mục [build] "
echo ""

cd RaftLib
mkdir [build]
cd [build]

echo ">> Tiến hành biên dịch "
echo ""

cmake ..

echo ""
echo ">> Tiến hành biên dịch và test: make && make test "
echo ""

make && make test

echo ""
echo ">> Tiến hành cài đặt: sudo make install "
echo ""

sudo make install

echo ""
echo ">> Xong"
echo ""