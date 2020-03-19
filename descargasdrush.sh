echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
apt-get install postgresql-11 -y

drush dl term_search
drush dl ctools
drush dl css_editor
drush dl date
drush dl event_log
drush dl feeds
drush dl google_analytics
drush dl workflow
drush dl ckeditor
drush dl galleryformatter
drush dl jquery_update
drush dl popup_message
drush dl submenutree
drush dl simple_ldap
drush dl smtp
drush dl i18n
drush dl site_map
drush dl token
drush dl panels
drush dl rules
drush dl metatag
drush dl captcha
drush dl variable
drush dl views
drush dl breakpoints

drush en term_search -y -y
drush en ctools -y
drush en css_editor -y
drush en date -y
drush en event_log -y
drush en feeds -y
drush en google_analytics -y
drush en workflow -y
drush en ckeditor -y
drush en galleryformatter -y
drush en jquery_update -y
drush en popup_message -y
drush en submenutree -y
drush en simple_ldap -y
drush en smtp -y
drush en i18n -y
drush en site_map -y
drush en token -y
drush en panels -y
drush en rules -y
drush en metatag -y
drush en captcha -y
drush en variable -y
drush en views -y
drush en breakpoints -y

drush en workflow_access -y
drush en workflow_vbo -y
drush en workflow -y          
drush en workflow_cleanup -y
drush en workflowfield -y
drush en workflownode -y           
drush en workflow_search_api -y  
drush en workflow_notify -y
drush en workflow_notify_og -y
drush en workflow_revert -y        
drush en workflow_rules -y             
drush en workflow_actions -y
drush en workflow_admin_ui -y
drush en workflow_views -y
drush en i18n_string -y
