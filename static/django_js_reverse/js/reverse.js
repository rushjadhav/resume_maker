this.Urls=(function(){var Urls={};var self={url_patterns:{}};var _get_url=function(url_pattern){return function(){var _arguments,index,url,url_arg,url_args,_i,_len,_ref,_ref_list,match_ref,provided_keys,build_kwargs;_arguments=arguments;_ref_list=self.url_patterns[url_pattern];if(arguments.length==1&&typeof(arguments[0])=="object"){var provided_keys_list=Object.keys(arguments[0]);provided_keys={};for(_i=0;_i<provided_keys_list.length;_i++)
provided_keys[provided_keys_list[_i]]=1;match_ref=function(ref)
{var _i;if(ref[1].length!=provided_keys_list.length)
return false;for(_i=0;_i<ref[1].length&&ref[1][_i]in provided_keys;_i++);return _i==ref[1].length;}
build_kwargs=function(keys){return _arguments[0];}}else{match_ref=function(ref)
{return ref[1].length==_arguments.length;}
build_kwargs=function(keys){var kwargs={};for(var i=0;i<keys.length;i++){kwargs[keys[i]]=_arguments[i];}
return kwargs;}}
for(_i=0;_i<_ref_list.length&&!match_ref(_ref_list[_i]);_i++);if(_i==_ref_list.length)
return null;_ref=_ref_list[_i];url=_ref[0],url_args=build_kwargs(_ref[1]);for(url_arg in url_args){url=url.replace("%("+url_arg+")s",url_args[url_arg]||'');}
return'/'+url;};};var name,pattern,self,url_patterns,_i,_len,_ref;url_patterns=[['accounts:my_profile',[['accounts/my_profile/',[]]],],['accounts:profile_pic',[['accounts/profile_pic/',[]]],],['accounts:signin',[['accounts/signin/',[]]],],['accounts:signout',[['accounts/signout/',[]]],],['accounts:signup',[['accounts/signup/',[]]],],['admin:app_list',[['admin/%(app_label)s/',['app_label',]]],],['admin:auth_group_add',[['admin/auth/group/add/',[]]],],['admin:auth_group_change',[['admin/auth/group/%(_0)s/',['_0',]]],],['admin:auth_group_changelist',[['admin/auth/group/',[]]],],['admin:auth_group_delete',[['admin/auth/group/%(_0)s/delete/',['_0',]]],],['admin:auth_group_history',[['admin/auth/group/%(_0)s/history/',['_0',]]],],['admin:index',[['admin/',[]]],],['admin:jsi18n',[['admin/jsi18n/',[]]],],['admin:login',[['admin/login/',[]]],],['admin:logout',[['admin/logout/',[]]],],['admin:password_change',[['admin/password_change/',[]]],],['admin:password_change_done',[['admin/password_change/done/',[]]],],['admin:profile_management_userprofile_add',[['admin/profile_management/userprofile/add/',[]]],],['admin:profile_management_userprofile_change',[['admin/profile_management/userprofile/%(_0)s/',['_0',]]],],['admin:profile_management_userprofile_changelist',[['admin/profile_management/userprofile/',[]]],],['admin:profile_management_userprofile_delete',[['admin/profile_management/userprofile/%(_0)s/delete/',['_0',]]],],['admin:profile_management_userprofile_history',[['admin/profile_management/userprofile/%(_0)s/history/',['_0',]]],],['admin:resume_management_resumetemplate_add',[['admin/resume_management/resumetemplate/add/',[]]],],['admin:resume_management_resumetemplate_change',[['admin/resume_management/resumetemplate/%(_0)s/',['_0',]]],],['admin:resume_management_resumetemplate_changelist',[['admin/resume_management/resumetemplate/',[]]],],['admin:resume_management_resumetemplate_delete',[['admin/resume_management/resumetemplate/%(_0)s/delete/',['_0',]]],],['admin:resume_management_resumetemplate_history',[['admin/resume_management/resumetemplate/%(_0)s/history/',['_0',]]],],['admin:sites_site_add',[['admin/sites/site/add/',[]]],],['admin:sites_site_change',[['admin/sites/site/%(_0)s/',['_0',]]],],['admin:sites_site_changelist',[['admin/sites/site/',[]]],],['admin:sites_site_delete',[['admin/sites/site/%(_0)s/delete/',['_0',]]],],['admin:sites_site_history',[['admin/sites/site/%(_0)s/history/',['_0',]]],],['admin:view_on_site',[['admin/r/%(content_type_id)s/%(object_id)s/',['content_type_id','object_id',]]],],['dashboard:index',[['dashboard/',[]]],],['display_resume',[['resume/%(access_url)s',['access_url',]]],],['resume:create_resume',[['rm/new_resume/',[]]],],['resume:list_templates',[['rm/templates/',[]]],],['resume:prepare_pdf',[['rm/pdf/%(id)s',['id',]]],],['resume:preview_template',[['rm/template_preview/%(id)s',['id',]]],],['resume:publish_resume',[['rm/publish_resume/%(id)s',['id',]]],],['resume:update_resume',[['rm/update_resume/%(name)s',['name',]]],],['website:index',[['',[]]]]];self.url_patterns={};for(_i=0,_len=url_patterns.length;_i<_len;_i++){_ref=url_patterns[_i],name=_ref[0],pattern=_ref[1];self.url_patterns[name]=pattern;Urls[name]=_get_url(name);Urls[name.replace(/-/g,'_')]=_get_url(name);}
return Urls;})();