drush dis term_search -y -y
drush dis ctools -y
drush dis css_editor -y
drush dis date -y
drush dis event_log -y
drush dis feeds -y
drush dis google_analytics -y
drush dis workflow -y
drush dis ckeditor -y
drush dis galleryformatter -y
drush dis jquery_update -y
drush dis popup_message -y
drush dis submenutree -y
drush dis simple_ldap -y
drush dis smtp -y
drush dis i18n -y
drush dis site_map -y
drush dis token -y
drush dis panels -y
drush dis rules -y
drush dis metatag -y
drush dis captcha -y
drush dis variable -y
drush dis views -y
drush dis breakpoints -y

drush dis workflow_access -y
drush dis workflow_vbo -y
drush dis workflow -y          
drush dis workflow_cleanup -y
drush dis workflowfield -y
drush dis workflownode -y           
drush dis workflow_search_api -y  
drush dis workflow_notify -y
drush dis workflow_notify_og -y
drush dis workflow_revert -y        
drush dis workflow_rules -y             
drush dis workflow_actions -y
drush dis workflow_admin_ui -y
drush dis workflow_views -y
drush dis i18n_string -y

a2dissite sitio1.conf sitio2.conf
systemctl stop apache2
mv /var/www/sitio1 /var/www/sitio1_old
mv /var/www/sitio2 /var/www/sitio2_old