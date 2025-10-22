exit
odoo -d wilkinsdb -u all --stop-after-init --db_host=db --db_user=odoo --db_password=odoo
ls /var/lib/odoo/.local/share/Odoo/filestore/wilkinsdb
odoo -d wilkinsdb -u all --stop-after-init --db_host=db --db_user=odoo --db_password=odoo --load-language=en_US
ls /var/lib/odoo/.local/share/Odoo/filestore/wilkinsdb
exit
rm -rf /var/lib/odoo/.local/share/Odoo/filestore/wilkinsdb/assets
odoo -d wilkinsdb -u all --stop-after-init --db_host=db --db_user=odoo --db_password=odoo
docker logs odoo-app -f
exit
chown -R odoo:odoo /mnt/extra-addons
exit
odoo -d wilkinsdb -u whatsapp_redirect --stop-after-init --db_host=db --db_user=odoo --db_password=odoo
exit
odoo -d wilkinsdb -u whatsapp_redirect --stop-after-init --db_host=db --db_user=odoo --db_password=odoo
exit
odoo -d wilkinsdb -u all --stop-after-init --db_host=db --db_user=odoo --db_password=odoo
exit
odoo -d wilkinsdb -u all --stop-after-init --db_host=db --db_user=odoo --db_password=odoo
chown -R odoo:odoo /var/lib/odoo/filestore
chown -R odoo:odoo /var/lib/odoo/filestore
exit
chown -R odoo:odoo /var/lib/odoo/filestore
exit
