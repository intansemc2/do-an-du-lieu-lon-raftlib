echo ""
echo ">> Xóa project cũ nếu đang tồn tại: "
echo ""

sudo rm -r ./RaftLib 

echo ""
echo ">> Clone project từ git về: "
echo ""

git clone https://github.com/RaftLib/RaftLib.git

echo ""
echo ">> Clone các git-dep đi kèm: "
echo ""

cd RaftLib/git-dep/

echo ""
echo ">> Clone affinity: "
echo ""

git clone https://github.com/RaftLib/affinity.git

echo ""
echo ">> Clone cmdargs: "
echo ""

git clone https://github.com/RaftLib/cmdargs.git

echo ""
echo ">> Clone demangle: "
echo ""

git clone https://github.com/RaftLib/demangle.git

echo ""
echo ">> Clone shm: "
echo ""

git clone https://github.com/RaftLib/shm.git

echo ""
echo ">> Xong"
echo ""