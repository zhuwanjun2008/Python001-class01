-- 创建用户，
CREATE USER maoyan IDENTIFIED BY '1qaz@WSX';

-- 配置权限
GRANT ALL PRIVILEGES ON maoyan.* TO 'maoyan'@'%';

-- 刷新权限
FLUSH PRIVILEGES;