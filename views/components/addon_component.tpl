<!-- prettier-ignore -->
% for addon_key, addon in services_and_prices_content['addon_section']['addons']['addon_default'].items():
<div class="w-full flex justify-center overflow-auto">
  <table class="table-auto w-full max-w-4xl text-left whitespace-no-wrap">
    <tbody>
      <tr class="align-middle">
        <!-- Title and Text -->
        <td class="text-unidDarkBlue p-4 text-left align-top w-2/3">
          <div class="space-y-1">
            <h5>{{ addon["info"]["title"] }}</h5>
            <p class="text-sm md:text-base lg:text-base xl:text-base">
              {{ addon["info"]["text"] }}
            </p>
          </div>
        </td>
        <!-- Price -->
        <td class="px-4 py-3 text-right align-middle w-1/3">
          <div class="flex justify-end items-center gap-2">
            <p
              class="text-unidDarkBlue text-xl xl:text-2xl font-saira font-bold"
            >
              {{ addon["info"]["price"] }}
            </p>
            <div class="flex flex-col text-xs text-unidDarkBlue text-right">
              <p>ekskl.</p>
              <p>moms</p>
            </div>
          </div>
        </td>
      </tr>
      <tr>
        <td colspan="2" class="border-b border-unidLightBlue"></td>
      </tr>
    </tbody>
  </table>
</div>
% end
