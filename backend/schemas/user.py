from typing import Optional, List

from pydantic import BaseModel, Field

from schemas.common import QueryData, ReadBase


class UserRole(BaseModel):
    uid: int = Field(description="用户id")
    rid: int = Field(description="角色id")


class UserRoleRead(UserRole, ReadBase):
    """用户 角色 读取模型"""

    pass


class UserBasic(BaseModel):
    username: str
    nickname: str
    limit_start: int | None
    limit_end: int | None


class UserIn(UserBasic):
    password: str


class UserRead(UserBasic, ReadBase):
    pass


class UserHasRole(BaseModel):
    """用户拥有角色"""

    id: int
    name: str
    status: int = Field(default=1, description="激活角色 5 正常 1 删除 9")


class UserInfo(UserRead):
    """用户信息模型"""

    roles: List[UserHasRole] = Field(..., description="用户拥有角色")
    limit_start: int | None = Field(..., description="登陆开始时间")
    limit_end: int | None = Field(..., description="登陆结束时间")


class RoleActive(BaseModel):
    rid: int = Field(description="角色id")
    status: int = Field(default=1, description="激活角色 5 正常 1 删除 9")


class UserAdd(UserIn):
    """新增用户模型"""

    roles: List[RoleActive] = Field(..., description="选择角色列表")
    limit_start: int | None = Field(..., description="登陆开始时间")
    limit_end: int | None = Field(..., description="登陆结束时间")


class UserQuery(QueryData):
    """查询模型"""

    username: Optional[str] = Field("", description="用户名")
    nickname: Optional[str] = Field("", description="姓名")


class UserPut(BaseModel):
    """用户更新模型"""

    nickname: str = Field(..., description="用户昵称")
    password: str = Field(..., description="密码")
    limit_start: int | None = Field(..., description="登陆开始时间")
    limit_end: int | None = Field(..., description="登陆结束时间")
    roles: List[RoleActive] = Field(..., description="选择角色列表")
